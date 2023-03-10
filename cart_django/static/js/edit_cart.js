function create_form() {
            
    // Create a form dynamically
    var form = document.createElement("form");
    form.setAttribute("method", "post");
    form.setAttribute("action", "");

    // Create an input element for emailID
    var ID = document.createElement("input");
    ID.setAttribute("type", "text");
    ID.setAttribute("name", "emailID");
    ID.setAttribute("placeholder", "E-Mail ID");

    // Create an input element for password
    var PWD = document.createElement("input");
    PWD.setAttribute("type", "password");
    PWD.setAttribute("name", "password");
    PWD.setAttribute("placeholder", "Password");

    // Create a submit button
    var s = document.createElement("input");
    s.setAttribute("type", "submit");
    s.setAttribute("value", "Submit");

    form.append(ID);
    form.append(PWD);
    form.append(s);

    document.getElementsByTagName("body")[0]
   .appendChild(form);
}