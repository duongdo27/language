var Answer = React.createClass({
  render: function() {
    if (this.props.num == 1) {
        var className = "btn btn-block btn-success";
    }
    else if (this.props.num == -1) {
        var className = "btn btn-block btn-danger";
    }
    else {
        var className = "btn btn-block";
    }

    return (
      <li>
      <button type="button" className={className} onClick={() => this.props.onClick()}>
        {this.props.value}
      </button>
      </li>
    );
  }
});


var Board = React.createClass({
    getInitialState: function(){
        return {
            data: data,
            num: 0,
            current_result: [0, 0, 0, 0],
            answered: false,
            finished: false
        }
    },

    handleClick: function(i) {
        if(this.state.answered){
            return;
        }
        var current_result = [0, 0, 0, 0];
        var correct = this.state.data[this.state.num][5];
        current_result[correct] = 1;
        if(i != correct){
            current_result[i] = -1;
        }
        this.setState({
            current_result: current_result,
            answered: true,
            finished: this.state.num == this.state.data.length - 1
        })
    },

    nextClick: function(evt) {
        this.setState({
            num: (this.state.num + 1),
            answered: false,
            current_result: [0, 0, 0, 0]
        })
    },

    doneClick: function(evt) {
    },

    render: function() {
        if(this.state.finished){
          var footer = <button className = "btn btn-info" onClick={this.doneClick}>Done</button>
        }
        else if(this.state.answered){
          var footer = <button className = "btn btn-warning" onClick={this.nextClick}>Next</button>
        }

        return (
            <div className="col-sm-6">
                 <h1 className="text-center">Question {this.state.num + 1}</h1>
                 <h3 className="text-center text-warning" dangerouslySetInnerHTML={{__html: this.state.data[this.state.num][0]}}></h3>
                 <ul>
                 <Answer value={this.state.data[this.state.num][1]}
                         onClick={() => this.handleClick(0)}
                         num={this.state.current_result[0]} />
                 <Answer value={this.state.data[this.state.num][2]}
                         onClick={() => this.handleClick(1)}
                         num={this.state.current_result[1]} />
                 <Answer value={this.state.data[this.state.num][3]}
                         onClick={() => this.handleClick(2)}
                         num={this.state.current_result[2]} />
                 <Answer value={this.state.data[this.state.num][4]}
                         onClick={() => this.handleClick(3)}
                         num={this.state.current_result[3]} />
                 </ul>
                 <div className="centered">{footer}</div>
            </div>
        )
    }
});

ReactDOM.render(
    <Board />,
    document.getElementById('container')
);