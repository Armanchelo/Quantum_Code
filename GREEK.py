griego = {
   'a': 'α',
   'b': 'β',
   'v': 'β',
   'g': 'γ',
   'd': 'δ',
   'ee': 'η',
   'e': 'ε',
   'z': 'ζ',
   'th': 'θ',
   't': 'θ',
   # 'ie': 'η',
   'i': 'ι',
   'k': 'κ',
   'q': 'κ',
   'l': 'λ',
   'm': 'μ',
   'n': 'ν',
   'ce': 'σ',
   'ci': 'σ',
   'cs': 'ξ',
   'ch': 'ξ',
   'cc': 'ξ',
   'c': 'κ',
   'x': 'ξ',
   'oo': 'ω',
   'o': 'ο',
   'ps': 'ψ',
   'ph': 'φ',
   'p': 'π',
   'rr': 'ρ',
   'r': 'ρ',
   's': 'σ',
   't': 'τ',
   'u': 'υ',
   'y': 'υ',
   'f': 'φ',
   'j': 'χ',
   'h': '' ,
   ' ': ' '
}

for letra, grieg in griego.copy().items():
   griego[letra.upper()] = grieg.upper()

griego['Ci'] = 'σ'
griego['Ce'] = 'σ'
upper = False
palabras = input('Palabra(s) a transcribir: ')
palabras = palabras.split(',')
resultados = []
for palabra in palabras:
   resultado = ''
   while palabra != '':
      for letra in griego:
         ln = len(letra)
         if letra == palabra[:len(letra)]:
            upper = palabra[:len(letra)].isupper()
            if letra not in ('ci', 'ce', 'CI', 'CE', 'Ci', 'Ce'):
               palabra = palabra[len(letra):]
            else:
               palabra = palabra[1:]
            r = griego[letra]
            if len(palabra) == 0 or palabra[0] == ' ':
               if r == 'σ':
                  resultado += 'ς'
               else:
                  resultado += r
            else:
               resultado += r
            break
      else:
         resultado += palabra[0]
         palabra = palabra[1:]
      # if upper:
      #    resultado = resultado[-ln:].upper()

   resultados += [resultado]

for resultado in resultados:   
   print(resultado)

