from django.shortcuts import render_to_response

# Create your views here.

# This is the function that is called by a url(...), in urls.py
def main_page(request):
    nameList = ['Noel', 'Cha']
    lastEditedBy = 'Cha'
    message1 = 'blablabla'
    message2 = 'Sup, Carl'
    # Display page without passing any variable
    # return render_to_response('index.html')
    
    # Display page while passing variables
    # by adding a "dictionary" argument like:
    # { 'nameInHtmlPage': variableName , 'nameInHtmlAgain': anotherVariableHere, ... }
    return render_to_response('index.html', { 'nameList': nameList , 'lastEditedBy': lastEditedBy, 'fromNoel': message1, 'fromCha': message2 })