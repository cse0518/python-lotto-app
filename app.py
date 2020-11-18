from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

lotto_numbers = list(range(1,46))

@app.route("/")
def hello():
    return render_template("index.html", variable=lotto)

@app.route("/lotto",methods=['GET'])
def lotto():
    lotto = select_numbers(6)
    return jsonify(lotto)

def select_numbers(select_amount:int):
    ## 01
    lotto = []
    for i in range(select_amount):
        while True:
            selected_num = random.randint(1,45)

            is_duplicated = False
            for num in lotto:
                if selected_num == num:
                    is_duplicated = True
                    break

            if is_duplicated:
                continue
            lotto.append(selected_num)
            break

    ## 02
    #candidate_numbers = lotto_numbers[:]
    #lotto = []
    #for i in range(select_amount):
    #    selected_num = candidate_numbers.pop(random.randrange(len(candidate_numbers)))
    #    lotto.append(selected_num)

    ## 03
    #lotto = random.sample(lotto_numbers, select_amount)

    return lotto

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
