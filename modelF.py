# display link_id to user/user_id1 ==> create a crud function that displays the link_id
# create a sign-up form for partner to input link_id & nomral registration fields
# update link based on link_id to add partner user_id into partner column
@app.route('/handle_answers', methods=['POST'])
def register_answers():
    """Create answers"""

    """
    get all question from db, variable named all_qs

    for every question in all_qs
        to get the user's answer, use request.form.get(question.id) # notice that we don't have "quotes" around question)
        print the answer to the question
    """
    user = crud.get_user_by_id(session['user_id'])
    all_questions = crud.get_questions()

    for question in all_questions:
        # print(question)
        answer=request.form.get(f"answer_to_{question.question_id}")
        print(answer)
        if answer:
            answer_obj= crud.create_answer(user, question, answer)
            print(answer_obj) ####HERE IS WHERE IS PRINTING ALL
        # make a sqlalchemy answer object using the answer
        # ..and your crud function to create answer obect/rows

    answer = request.form.get("answer")
    wish = request.form.get("wish")  
    question_id = request.form.get("question_id")
    print("\n"* 2, "*" * 5, answer)

    user = crud.get_user_by_id(session['user_id'])
    question = crud.get_question_by_id(question_id)
    answers = crud.get_answer_by_id(session['user_id'])
    

    if answer:
        answer = crud.create_answer(user, question, answer)
        return render_template('answer_details.html', answer=answer)### HERE IS WHERE IS PRINTING ONE AND I CAN SEE IT!!!
    
    if wish:
        wish = crud.get_wish(wish)
        flash('You have a wish!')
        return render_template('my_wishes.html', wish=wish)
    if answer and wish:
        flash("Let's check your answers")
        return redirect('/welcome')

@app.route('/answers')
def show_answers():
    """Show the answers from user"""

    answers = crud.get_answer_by_id(session['user_id'])
    all_answers = []

    for ans in all_answers:
        question_answer = crud.get_question_text_by_id(answer.question_id)
        answer_text = ans.answer
        all_answers.append([answer_text, question_answer])

    return render_template('answer_details.html', all_answers=all_answers)

@app.route('/questions')


return render_template('answer_details.html', answers=answers, answer=answer, a=a, user_id=user_id)


WISHES WORKING BUT CANT SEE them

@app.route('/wish')
def wishes_form():
    """Form to get wishes data"""

    wishes = request.args.get('wish')

    return render_template('my_wishes.html')

@app.route('/wish', methods=['POST'])
def register_wishes():
    """Create wishes"""

    
    wish = request.form.get("wish")
    print('*******', wish, '******')

    if wish:
        wishes = crud.create_wish(wish)
        wish = crud.get_wish(wish)
        return render_template('show_wishes.html', wish=wish)

@app.route('/view-wishes')
def view_user_wishes(wish):
    """User can view wishes"""

    wish = crud.get_wish(wish)


    return render_template('show_wishes.html', wish=wish)