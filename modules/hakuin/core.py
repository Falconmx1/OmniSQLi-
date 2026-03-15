# modules/hakuin/core.py
"""
Hakuin - Blind SQL Injection Optimization Framework
Uses language models to guess data faster
"""

import random
import string
from typing import List, Dict, Optional
from collections import Counter
import math

class LanguageModel:
    """Modelo de lenguaje simple para adivinar palabras"""
    
    def __init__(self):
        # Frecuencias de letras en español/inglés
        self.char_freq = {
            'a': 0.12, 'b': 0.02, 'c': 0.04, 'd': 0.05, 'e': 0.13,
            'f': 0.01, 'g': 0.01, 'h': 0.01, 'i': 0.06, 'j': 0.01,
            'k': 0.01, 'l': 0.04, 'm': 0.02, 'n': 0.07, 'o': 0.08,
            'p': 0.02, 'q': 0.01, 'r': 0.06, 's': 0.06, 't': 0.05,
            'u': 0.03, 'v': 0.01, 'w': 0.01, 'x': 0.01, 'y': 0.01,
            'z': 0.01
        }
        
        # Palabras comunes en bases de datos
        self.common_words = [
            'admin', 'user', 'password', 'username', 'email',
            'name', 'id', 'date', 'time', 'status', 'role',
            'active', 'created', 'updated', 'session', 'token'
        ]
    
    def predict_next_char(self, context: str) -> Dict[str, float]:
        """Predice el siguiente caracter basado en el contexto"""
        
        if not context:
            # Si no hay contexto, usar frecuencias generales
            return self.char_freq.copy()
        
        # Buscar palabras comunes que coincidan con el inicio
        predictions = {}
        for word in self.common_words:
            if word.startswith(context.lower()):
                if len(word) > len(context):
                    next_char = word[len(context)]
                    predictions[next_char] = predictions.get(next_char, 0) + 1
        
        # Normalizar
        if predictions:
            total = sum(predictions.values())
            return {k: v/total for k, v in predictions.items()}
        
        # Fallback a frecuencias generales
        return self.char_freq.copy()

class HakuinExtractor:
    """Motor de extracción optimizada para Blind SQLi"""
    
    def __init__(self):
        self.lm = LanguageModel()
        self.queries_made = 0
        self.cache = {}
    
    def extract_string(self, oracle_func, max_length: int = 50) -> str:
        """
        Extrae un string usando predicciones del modelo de lenguaje
        oracle_func: función que recibe (posicion, char) y retorna True/False
        """
        result = []
        
        for pos in range(max_length):
            # Obtener predicciones para el siguiente carácter
            context = ''.join(result)
            predictions = self.lm.predict_next_char(context)
            
            # Ordenar por probabilidad
            sorted_chars = sorted(predictions.items(), key=lambda x: -x[1])
            
            found = False
            for char, prob in sorted_chars:
                self.queries_made += 1
                if oracle_func(pos, char):
                    result.append(char)
                    found = True
                    break
            
            if not found:
                # Si no encontramos con predicciones, fuerza bruta
                for char in string.printable:
                    if char in predictions:
                        continue  # Ya lo intentamos
                    
                    self.queries_made += 1
                    if oracle_func(pos, char):
                        result.append(char)
                        found = True
                        break
                
                if not found:
                    # Llegamos al final del string
                    break
        
        return ''.join(result)
    
    def extract_int(self, oracle_func, max_bits: int = 32) -> int:
        """Extrae un entero usando búsqueda binaria optimizada"""
        
        # Determinar rango usando técnica de potencias
        low, high = 0, 1
        
        # Encontrar límite superior
        while True:
            self.queries_made += 1
            if oracle_func(high):
                low = high
                high *= 2
            else:
                break
            
            if high > 2**max_bits:
                high = 2**max_bits
                break
        
        # Búsqueda binaria en el rango encontrado
        while low < high:
            mid = (low + high) // 2
            self.queries_made += 1
            
            if oracle_func(mid):
                low = mid + 1
            else:
                high = mid
        
        return low
    
    def extract_table_names(self, oracle_func) -> List[str]:
        """Extrae nombres de tablas usando el modelo"""
        tables = []
        num_tables = self.extract_int(lambda n: self._table_exists(oracle_func, n))
        
        for i in range(num_tables):
            table_name = self.extract_string(lambda pos, char: 
                self._table_char_at(oracle_func, i, pos, char))
            tables.append(table_name)
        
        return tables
    
    def _table_exists(self, oracle_func, index: int) -> bool:
        """Simula verificación de existencia de tabla"""
        # En implementación real, esto haría queries SQL
        return index < 5  # Simulado
    
    def _table_char_at(self, oracle_func, table_index: int, pos: int, char: str) -> bool:
        """Simula verificación de caracter en nombre de tabla"""
        # En implementación real, esto haría queries SQL
        common_tables = ['users', 'admins', 'products']
        if table_index < len(common_tables):
            table = common_tables[table_index]
            if pos < len(table):
                return table[pos] == char
        return False

class HakuinOptimizer:
    """Optimizador principal de Hakuin"""
    
    def __init__(self):
        self.extractor = HakuinExtractor()
    
    def run_blind_extraction(self, target_url: str, param: str) -> Dict:
        """Ejecuta extracción optimizada en objetivo Blind SQLi"""
        
        print("[Hakuin] Iniciando extracción optimizada...")
        
        # Función oracle simulada (en realidad haría peticiones HTTP)
        def oracle_simulator(position, char):
            # Simula una Blind SQLi donde la tabla es 'users'
            target = 'users'
            if position < len(target):
                return target[position] == char
            return False
        
        # Extraer datos
        result = self.extractor.extract_string(oracle_simulator)
        
        return {
            'extracted_data': result,
            'queries_made': self.extractor.queries_made,
            'method': 'hakuin_optimized',
            'efficiency': f"~{len(result)} chars in {self.extractor.queries_made} queries"
        }

if __name__ == "__main__":
    optimizer = HakuinOptimizer()
    results = optimizer.run_blind_extraction("http://test.com/page.php?id=1", "id")
    
    print(f"\n[+] Datos extraídos: {results['extracted_data']}")
    print(f"[+] Queries realizadas: {results['queries_made']}")
