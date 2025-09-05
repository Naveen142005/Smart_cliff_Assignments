class NoAnswerError extends Error {
    constructor(msg) {
        super(msg);
    }
}

class InvalidInputError extends Error {
    constructor(msg) {
        super(msg);
    }
}

class TimeUpError extends Error {
    constructor(msg) {
        super(msg);
    }
}

function submitAnswer(str, time = false) {
    try {
        if (str == null) 
            throw new NoAnswerError("No answer selected.Please choose a option");
        if (isNaN(Number(str))) 
            throw new InvalidInputError("Invalid input.Answer must be  number");
        if (time) 
            throw new TimeUpError("Exam time is over.Submission not allowed");

        console.log(`Answer ${str} submitted successfully.`);
    } catch (err) {
        console.log(err.message);
    }
}

submitAnswer(null);
submitAnswer('A');
submitAnswer('2', true);
submitAnswer(2);
