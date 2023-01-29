from gtts import gTTS
import os

ans = ''

# msg -> message from you
# ans -> answer from the machine

# understand context to choose a function to get answer


from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline



con = '''

'''
while True:
    msg = input('> ')
    if msg == '':
        break

    model_name = "deepset/roberta-base-squad2"

    # a) Get predictions
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
    QA_input = {
        'question': msg,
        'context': con
    }
    res = nlp(QA_input)

    # b) Load model & tokenizer
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    ans = res['answer']

    # TAKE MSG AND PASS INTO AI MODEL THAT UNDERSTANDS CONTEXT
    # THEN, BASED ON THE ANSWER IT WILL CHOOSE A FUNCTION THAT GIVES AN ANSWER

    # EX. 'GREETING' "HI" OR ANYTHING ELSE THAT DOESNT MATCH ANYTHING
    # ANSWERS WITH "HI BOSS" OR "HI FERNANDO, GOOD MORNING"
    # OR WHATEVER, PERSONALITY AND BLA BLA BLA

    # SPECIFIC FUNCTIONS AND INTEGRATIONS WILL COME IN LATER

    # AT FIRST IT WILL BE A PYTHON EXECUTABLE IN TERMINAL WITH INPUT COMMANDS OR VOICE WHATEVER

    # A LOT OF QUESTIONS NEED TO BE ANSWERED

    # SPEECH
    # ------------------------
    language = 'en'
    obj = gTTS(text=ans, lang=language, slow=False)
    obj.save("speech.mp3")
    os.system("speech.mp3")
    # ------------------------
    print('> '+ans)