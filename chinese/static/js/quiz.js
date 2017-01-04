var Answer = React.createClass({
    displayName: "Answer",

    render: function () {
        if (this.props.num == 1) {
            var className = "btn btn-block btn-success";
        } else if (this.props.num == -1) {
            var className = "btn btn-block btn-danger";
        } else {
            var className = "btn btn-block";
        }

        return React.createElement(
            "li",
            null,
            React.createElement(
                "button",
                { type: "button", className: className, onClick: () => this.props.onClick() },
                this.props.value
            )
        );
    }
});

var Board = React.createClass({
    displayName: "Board",

    getInitialState: function () {
        return {
            data: data,
            num: 0,
            current_result: [0, 0, 0, 0],
            answered: false,
            finished: false,
            scores: []
        };
    },

    handleClick: function (i) {
        if (this.state.answered) {
            return;
        }
        var current_result = [0, 0, 0, 0];
        var correct = this.state.data[this.state.num][5];
        current_result[correct] = 1;

        var current_score = 1;
        if (i != correct) {
            current_result[i] = -1;
            var current_score = 0;
        }

        var new_scores = this.state.scores.slice(0);
        new_scores.push(current_score);

        this.setState({
            current_result: current_result,
            answered: true,
            finished: this.state.num == this.state.data.length - 1,
            scores: new_scores
        });
    },

    nextClick: function (evt) {
        this.setState({
            num: this.state.num + 1,
            answered: false,
            current_result: [0, 0, 0, 0]
        });
    },

    doneClick: function (evt) {
        $.ajax({
            type: 'POST',
            url: "/quiz_submit",
            data: { 'data': JSON.stringify({
                    'scores': this.state.scores,
                    'ideographs': this.state.data.map(function (x) {
                        return x[6];
                    })
                }) }
        });
        window.location.href = success_url;
    },

    render: function () {
        if (this.state.finished) {
            var footer = React.createElement(
                "button",
                { className: "btn btn-info", onClick: this.doneClick },
                "Done"
            );
        } else if (this.state.answered) {
            var footer = React.createElement(
                "button",
                { className: "btn btn-warning", onClick: this.nextClick },
                "Next"
            );
        }

        var total_score = this.state.scores.reduce(function (a, b) {
            return a + b;
        }, 0);

        return React.createElement(
            "div",
            { className: "col-sm-6" },
            React.createElement(
                "h1",
                { className: "text-center" },
                "Question ",
                this.state.num + 1
            ),
            React.createElement(
                "h2",
                { className: "text-center text-info" },
                "Corrects: ",
                total_score,
                "/",
                this.state.data.length
            ),
            React.createElement("h3", { className: "text-center text-warning", dangerouslySetInnerHTML: { __html: this.state.data[this.state.num][0] } }),
            React.createElement(
                "ul",
                null,
                React.createElement(Answer, { value: this.state.data[this.state.num][1],
                    onClick: () => this.handleClick(0),
                    num: this.state.current_result[0] }),
                React.createElement(Answer, { value: this.state.data[this.state.num][2],
                    onClick: () => this.handleClick(1),
                    num: this.state.current_result[1] }),
                React.createElement(Answer, { value: this.state.data[this.state.num][3],
                    onClick: () => this.handleClick(2),
                    num: this.state.current_result[2] }),
                React.createElement(Answer, { value: this.state.data[this.state.num][4],
                    onClick: () => this.handleClick(3),
                    num: this.state.current_result[3] })
            ),
            React.createElement(
                "div",
                { className: "centered" },
                footer
            )
        );
    }
});

ReactDOM.render(React.createElement(Board, null), document.getElementById('container'));