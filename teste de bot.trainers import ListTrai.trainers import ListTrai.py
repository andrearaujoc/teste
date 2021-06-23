from chatterbot.trainers import ListTrainer
from chatterbot import chatterbot
#inicio do codigo 
bot.set_trainer(ListTrainer)
bot.train(conversa)
while true:
 pergunta =  input("Usuário:")
 resposta = bot.get_response(pergunta)   
 if float(resposta.confidente) > 0.5:
     print('TW Bot:', resposta)
     else:
       print('TW Bot: Ainda não sei responder esta pergunta')
       

       



