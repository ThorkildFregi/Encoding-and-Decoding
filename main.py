from flask import Flask, url_for, redirect, render_template, request, session
import random

app = Flask(__name__)
secretKey = random.randint(1, 100)
secretKey = str(secretKey)
app.secret_key = secretKey
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890çéèàâûîïü"

@app.route('/')
def back_To_Accueil():
    return redirect(url_for('accueil'))

@app.route('/Accueil')
def accueil():
    return render_template("accueil.html")

@app.route('/Traitement', methods=['post'])
def traitement():
    newMessage = ''
    message = request.form['message']
    key = request.form['key']
    key = int(key)
    for character in message:
          if character in alphabet:
              position = alphabet.find(character)
              newPosition = (position + key) % 71
              newCharacter = alphabet[newPosition]
              newMessage += newCharacter
          else:
               newMessage += character
    session['newMessage'] = newMessage
    return redirect(url_for('newMessage'))

@app.route('/NouveauMessage', methods=['GET' , 'POST'])
def newMessage():
    newMessage = session.get('newMessage', None)
    return render_template('newMessage.html', newMessage=newMessage)
