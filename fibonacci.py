from flask import Flask
app = Flask(__name__)

@app.route("/fib/<int:i>")
def fib(i):
    Number = i
    a = 0
    b = 1
    c = 0

    for  i in range(Number-1):
        a = b
        b = c
        c = a + b
        return c

if __name__ == "__main__":
    app.run()