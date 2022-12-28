"""Tecnicas de debug
1. rodar o script com a opcao '-i' do python para executar em modo iterativo
   # python3 -i script.py

2. utilizar print() estrategicos no script para entender o que esta acontecendo

3. utilizar a ferramenta pdb (python debug) que esta disponivel nativamente no
   python
   # python3 -m pdb script.py
   # (Pdb) help
   e.g:
       l (line)
       n (next)
       s (step in - entra na funcao)
       b $line (break point)
       disable $line (disable a break point)

4. colocar breakpoints no proprio codigo
   import pdb
   pdb.set_trace()
   
   or
   
   breakpoint() # Python3.7 ou superior

5. utilizar implementacao diferentes do pbd
   # pip install ipbd
   # python3 -m ipdb script.py
   
   para usar o ipdb como a ferramenta default de debug exportar a variavel
   PYTHONBREAKPOINT
   # export PYTHONBREAKPOINT=ipdb.set_trace
   
6. utilizar o pudb
   # python3 -m pudb script.py
"""
