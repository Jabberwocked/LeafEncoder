from flask import Flask

from LeafNameEncoder.Leaf import Leaf
from LeafNameEncoder.ValueTypes.ValueTypeMap import ValueType

app = Flask(__name__)

@app.route('/')
def index():
    sut = Leaf()
    values = [(ValueType.DayHour, (5, 17)), (ValueType.UInt, 2294967295)]
    # act
    return sut.create(values)

if __name__ == '__main__':
    app.run()