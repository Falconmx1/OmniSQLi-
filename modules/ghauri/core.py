# modules/ghauri/core.py
"""
Ghauri - Advanced SQL Injection Tool
Specialized in complex requests (JSON/XML) and authentication
"""

import json
import xml.etree.ElementTree as ET
import requests
from typing import Dict, Any, Optional
import re

class RequestHandler:
    """Maneja peticiones complejas con diferentes content-types"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def send_request(self, url: str, method: str = 'GET', 
                     data: Any = None, content_type: str = 'application/x-www-form-urlencoded') -> Dict:
        """Envía petición con manejo inteligente de content-type"""
        
        headers = {'Content-Type': content_type}
        
        # Preparar datos según content-type
        if content_type == 'application/json' and data:
            if isinstance(data, str):
                data = json.loads(data)
            data = json.dumps(data)
        
        elif content_type == 'application/xml' and data:
            if isinstance(data, dict):
                data = self._dict_to_xml(data)
        
        # Enviar petición
        try:
            if method.upper() == 'GET':
                response = self.session.get(url, params=data, headers=headers, timeout=10)
            else:
                response = self.session.post(url, data=data, headers=headers, timeout=10)
            
            return {
                'status_code': response.status_code,
                'headers': dict(response.headers),
                'content': response.text,
                'url': response.url
            }
        except Exception as e:
            return {'error': str(e)}
    
    def _dict_to_xml(self, data: Dict, root_name: str = 'root') -> str:
        """Convierte diccionario a XML"""
        root = ET.Element(root_name)
        
        for key, value in data.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        
        return ET.tostring(root, encoding='unicode')

class JSONInjector:
    """Especialista en inyección sobre JSON"""
    
    def __init__(self, request_handler: RequestHandler):
        self.handler = request_handler
    
    def test_injection_points(self, json_data: Dict) -> List[Dict]:
        """Identifica puntos inyectables en JSON"""
        vulnerable_points = []
        
        def recursive_check(data, path=""):
            if isinstance(data, dict):
                for key, value in data.items():
                    current_path = f"{path}.{key}" if path else key
                    
                    # Probar inyección en valores
                    if isinstance(value, str):
                        if self._test_payload(current_path, value):
                            vulnerable_points.append({
                                'path': current_path,
                                'type': 'string',
                                'original': value
                            })
                    
                    recursive_check(value, current_path)
            
            elif isinstance(data, list):
                for i, item in enumerate(data):
                    recursive_check(item, f"{path}[{i}]")
        
        recursive_check(json_data)
        return vulnerable_points
    
    def _test_payload(self, path: str, original: str) -> bool:
        """Prueba si el punto es vulnerable"""
        # Simulación - en realidad haría peticiones
        test_payloads = ["'", "\"", "1' AND '1'='1", "1' AND '1'='2"]
        return len(test_payloads) > 0  # Simplificado

class AdvancedGhauri:
    """Clase principal de Ghauri"""
    
    def __init__(self):
        self.handler = RequestHandler()
        self.json_injector = JSONInjector(self.handler)
        self.results = {}
    
    def scan(self, url: str, method: str = 'POST', 
             data: Dict = None, content_type: str = 'application/json'):
        """Escaneo completo con Ghauri"""
        
        print(f"[Ghauri] Escaneando: {url}")
        print(f"[Ghauri] Content-Type: {content_type}")
        
        # Enviar petición inicial
        response = self.handler.send_request(url, method, data, content_type)
        
        if 'error' in response:
            print(f"[!] Error: {response['error']}")
            return None
        
        # Detectar puntos de inyección según content-type
        if content_type == 'application/json' and data:
            points = self.json_injector.test_injection_points(data)
            self.results['json_points'] = points
            print(f"[+] Puntos JSON vulnerables: {len(points)}")
        
        # Detectar DBMS por fingerprints
        dbms = self._detect_dbms(response['content'])
        self.results['dbms'] = dbms
        print(f"[+] DBMS detectado: {dbms}")
        
        return self.results
    
    def _detect_dbms(self, content: str) -> str:
        """Detecta DBMS por errores característicos"""
        signatures = {
            'MySQL': ['mysql_fetch', 'MySQLSyntaxError', 'Incorrect syntax near'],
            'MSSQL': ['Microsoft OLE DB', 'SQL Server', 'Driver::'], 
            'Oracle': ['ORA-', 'Oracle error', 'PLS-'],
            'PostgreSQL': ['PostgreSQL', 'pg_', 'ERROR:']
        }
        
        for dbms, sigs in signatures.items():
            for sig in sigs:
                if sig.lower() in content.lower():
                    return dbms
        
        return 'Unknown'

if __name__ == "__main__":
    # Ejemplo de uso
    ghauri = AdvancedGhauri()
    
    test_json = {
        "username": "admin",
        "password": "12345",
        "filters": {
            "active": True,
            "role": "user"
        }
    }
    
    results = ghauri.scan(
        url="http://test.com/api/login",
        method="POST",
        data=test_json,
        content_type="application/json"
    )
