const wishes = {{ answer.wish }}
ReactDom.render(
    React.createElement(App, wishes),
    document.getElementById('wishes')
);
 
 

/* when button click, wishes will pop up and will be check when task is done */