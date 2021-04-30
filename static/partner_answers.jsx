function Answers(props) {

    const [questions, setAnswers] = React.useState([])

    React.useEffect(() => {
        $.get('/answers_partner', (result) => {
            setAnswers(result);
        });
    }, [])
}