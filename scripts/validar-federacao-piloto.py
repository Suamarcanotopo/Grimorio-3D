#!/usr/bin/env python3
"""Static, fail-closed checks for SIN-FED-001 offline WebGL demo.
Does NOT attest image quality, browser runtime, provider inference or commercial success.
"""
from pathlib import Path
from html.parser import HTMLParser
import re

ROOT=Path(__file__).resolve().parents[1]
DOC=ROOT/"EXEMPLOS/FEDERACAO-SIN-PILOTO-001.html"
GUIDE=ROOT/"EXEMPLOS/FEDERACAO-SIN-PILOTO-001.md"

class Inspect(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=[]
        self.external=[]
        self.canvas=0
        self.lang=None
        self.script_inline=0
        self.links=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if "id" in d:self.ids.append(d["id"])
        if tag=="html":self.lang=d.get("lang")
        if tag=="canvas":self.canvas+=1
        if tag in ("script","iframe","link","img","source","video","audio"):
            for key in ("src","href"):
                if d.get(key):self.external.append((tag,d[key]))
        if tag=="script" and not d.get("src"):self.script_inline+=1
        if tag=="a":self.links.append(d.get("href"))

text=DOC.read_text(encoding="utf-8")
guide=GUIDE.read_text(encoding="utf-8")
parse=Inspect();parse.feed(text)
assert parse.lang=="pt-BR",parse.lang
assert parse.canvas==1 and parse.script_inline==1
assert not parse.external,parse.external
assert len(parse.ids)==len(set(parse.ids)),"IDs duplicados"
for name in ("objeto","esquerda","direita","pausa","fallback","criterios"):
    assert name in parse.ids,name
for link in parse.links:
    assert link and link.startswith("#") and link[1:] in parse.ids,link
for method in ("getContext('webgl'","createShader(","compileShader(","drawArrays(","requestAnimationFrame(","pointerdown","keydown","matchMedia(","prefers-reduced-motion"):
    assert method in text,method
for dangerous in ("fetch(","XMLHttpRequest","localStorage","sessionStorage","document.cookie","eval(","Function("):
    assert dangerous not in text,dangerous
assert text.count("gl_Position=vec4(")==1
for marker in ("Grimorio-SIN","ListOFprompts","Grimorio-3D","grimorio-skills","NOT_RUN","R2","Coliseum","Governance Guard"):
    assert marker.lower() in guide.lower(),marker
assert "<script src=" not in text and "<iframe" not in text
print("PASS: offline WebGL candidate, keyboard/buttons/fallback, four canonical sources, no external payloads")
print("LIMIT: browser rendering, accessibility audit, provider/image generation and sales are NOT VERIFIED")
