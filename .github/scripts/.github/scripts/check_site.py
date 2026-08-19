#!/usr/bin/env python3
"""
Verificações básicas de qualidade para o site da Gungo Agência & Marketing.
Corre automaticamente em cada Pull Request, antes de aceitar o merge.
Não precisa de Node.js nem de build — só Python (já vem no GitHub Actions).
"""
import sys
import re

ERROS = []
AVISOS = []

FICHEIROS_OBRIGATORIOS = ["index.html", "admin.html", "firebase-config.js"]

def ler(caminho):
    try:
        with open(caminho, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None

def verificar_ficheiros_existem():
    for ficheiro in FICHEIROS_OBRIGATORIOS:
        if ler(ficheiro) is None:
            ERROS.append(f"Ficheiro obrigatório em falta: {ficheiro}")

def verificar_tags_balanceadas(caminho, conteudo):
    for tag in ["html", "head", "body", "div", "section", "script", "style"]:
        abertos = len(re.findall(rf"<{tag}(?:\s[^>]*)?>", conteudo))
        fechados = len(re.findall(rf"</{tag}>", conteudo))
        if abertos != fechados:
            ERROS.append(
                f"{caminho}: tag <{tag}> desequilibrada "
                f"(aberturas={abertos}, fechos={fechados})"
            )

def verificar_placeholders_esquecidos(caminho, conteudo):
    if "COLA_AQUI" in conteudo:
        sem_sentry = conteudo.replace("COLA_AQUI_O_DSN_DA_SENTRY", "")
        if "COLA_AQUI" in sem_sentry:
            AVISOS.append(f"{caminho}: contém um placeholder por preencher ('COLA_AQUI...')")

def verificar_javascript_basico(caminho, conteudo):
    scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", conteudo, re.S)
    for i, s in enumerate(scripts):
        if "src=" in s:
            continue
        if s.count("{") != s.count("}"):
            ERROS.append(f"{caminho}: script #{i} tem chavetas desequilibradas")
        if s.count("(") != s.count(")"):
            ERROS.append(f"{caminho}: script #{i} tem parênteses desequilibrados")

def main():
    verificar_ficheiros_existem()

    for ficheiro in ["index.html", "admin.html"]:
        conteudo = ler(ficheiro)
        if conteudo is None:
            continue
        verificar_tags_balanceadas(ficheiro, conteudo)
        verificar_placeholders_esquecidos(ficheiro, conteudo)
        verificar_javascript_basico(ficheiro, conteudo)

    print("=" * 60)
    print("VERIFICAÇÃO DO SITE — GUNGO AGÊNCIA & MARKETING")
    print("=" * 60)

    if AVISOS:
        print(f"\n⚠️  {len(AVISOS)} aviso(s) (não bloqueiam o merge):")
        for a in AVISOS:
            print(f"   - {a}")

    if ERROS:
        print(f"\n❌ {len(ERROS)} erro(s) encontrado(s):")
        for e in ERROS:
            print(f"   - {e}")
        print("\nCorrige estes pontos antes de fazer merge.")
        sys.exit(1)

    print("\n✅ Tudo certo! Nenhum erro estrutural encontrado.")
    sys.exit(0)

if __name__ == "__main__":
    main()
