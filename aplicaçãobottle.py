from bottle import Bottle, run

app = Bottle()

msg = '''
<center><h1>Minha página web</h1></center>
<p><center>Bem vindo a minha primeira pagina web utilizando Bottle</center></p>
<center><a href="/pagina_web">Clique aqui para redirecionar a outra página</a></center>
'''
@app.route('/')
def index():
     return msg

@app.route('/pagina_web')
def pagina():
     return '<center><h1>Bem vindo a minha aplicação Web</h1></center>\
             <center><a href="/">Voltar a pagina principal</a></center>'
run(app, host='localhost', port=8080)

