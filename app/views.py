from django.shortcuts import render
import database as db

# Create your views here.
def home(request):
    return render(request, "index.html", {"verbs":db.get_all_verbs()})

def test(request):
    if request.method == 'POST':
        verb = request.POST['verb']
        response = str(request.POST['response']).lower()
        db_verb = db.get_verb_by_infinitive(verb)
        correct = db_verb[2] + " " + db_verb[1]
        if response == correct:
            return render(request, "test.html", {"verb":db.get_random_verb(), "warnings":[("", "", "Correct", "good")]})
        else:
            return render(request, "test.html", {"verb":db_verb, "warnings":[(response, " is incorrect! The solution is", correct, "bad")]})
    return render(request, "test.html", {"verb":db.get_random_verb()})

def add(request):
    if request.method == 'POST':
        infinitive = request.POST['infinitive']
        firstPersonPast = request.POST['FrstPrsnPast']
        before = request.POST['before']

        if db.get_verb_by_infinitive(infinitive) != None:
            return render(request, "add.html", {"warnings": [(infinitive, " is allready in the database", "bad")]})
        db.add_verb(infinitive, firstPersonPast, before)
        return render(request, "add.html", {"warnings": [(infinitive, " added into the database", "good")]})
    return render(request, "add.html")