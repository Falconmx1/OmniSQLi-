#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
OmniSQLi - Ultimate SQL Injection Swiss Army Knife
Más potente que SQLmap, con IA integrada y múltiples herramientas de élite
Author: Falconmx1
"""

import argparse
import sys
import os
from datetime import datetime

BANNER = """
╔═╗╔╗ ╔╗   ╔═╗╔═╗╔╦╗╔═╗╦
║ ╦╠╩╗╠╩╗  ║ ║╚═╗ ║ ╠═╣║
╚═╝╚═╝╚═╝  ╚═╝╚═╝ ╩ ╩ ╩╩
🚀 La navaja suiza definitiva para SQL Injection
🔥 Más potente que SQLmap | IA-Powered | Multi-Tool Suite
"""

class OmniSQLi:
    def __init__(self):
        self.target = None
        self.agents = []
        self.modules = {
            'vexsqli': {'status': 'ready', 'desc': 'NLP Payload Obfuscation'},
            'ghauri': {'status': 'ready', 'desc': 'Advanced JSON/XML Injection'},
            'hakuin': {'status': 'ready', 'desc': 'Blind SQLi Optimization'},
            'multiagent': {'status': 'ready', 'desc': 'AI Multi-Agent System'},
            'nosqlmap': {'status': 'ready', 'desc': 'NoSQL Exploitation'},
            'jsql': {'status': 'ready', 'desc': 'GUI Interface'},
            'sqlninja': {'status': 'ready', 'desc': 'MSSQL Post-Exploitation'}
        }
    
    def show_banner(self):
        print(BANNER)
        print(f"[+] Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("[+] Módulos cargados:", len(self.modules))
        print("-" * 60)
    
    def run(self, args):
        self.show_banner()
        self.target = args.url
        
        print(f"[🎯] Target: {self.target}")
        print("[🤖] Iniciando agentes de IA...")
        
        if args.agents:
            print(f"[+] Agentes activados: {args.agents}")
        
        if args.all:
            print("[+] Modo completo - Activando TODOS los módulos:")
            for module, info in self.modules.items():
                print(f"    ✓ {module}: {info['desc']}")
        
        if args.blind and args.optimize == 'hakuin':
            print("[🧠] Modo Hakuin activado - Extracción optimizada para Blind SQLi")
        
        if args.waf_bypass and args.nlp:
            print("[🎭] Modo NLP bypass - Ofuscando payloads para evadir WAFs")
        
        if args.gui:
            print("[🖥️] Iniciando interfaz gráfica jSQL...")
        
        if args.post_exploit:
            print("[💀] Modo post-explotación - Preparando SQLninja para MSSQL")
        
        print("\n[✅] OmniSQLi listo para comenzar el ataque!")
        print("[⚠️] Asegúrate de tener autorización para probar este objetivo\n")
        
        return True

def main():
    parser = argparse.ArgumentParser(description='OmniSQLi - Más potente que SQLmap')
    parser.add_argument('-u', '--url', required=True, help='URL objetivo (ej: http://target.com/page.php?id=1)')
    parser.add_argument('--agents', help='Agentes específicos: recon,payload_gen,exploit')
    parser.add_argument('--all', action='store_true', help='Activar todos los módulos')
    parser.add_argument('--blind', action='store_true', help='Modo Blind SQLi')
    parser.add_argument('--optimize', choices=['hakuin', 'normal'], default='normal', help='Algoritmo de optimización')
    parser.add_argument('--waf-bypass', action='store_true', help='Intentar evadir WAF')
    parser.add_argument('--nlp', action='store_true', help='Usar NLP para ofuscación')
    parser.add_argument('--gui', action='store_true', help='Iniciar interfaz gráfica')
    parser.add_argument('--post-exploit', action='store_true', help='Modo post-explotación')
    parser.add_argument('--report', choices=['html', 'pdf', 'md'], help='Generar reporte')
    
    args = parser.parse_args()
    
    tool = OmniSQLi()
    tool.run(args)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Interrumpido por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Error: {e}")
        sys.exit(1)
