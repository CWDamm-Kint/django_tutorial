from polls.models import Choice, Question

print(Question.objects.all())
print(Question.objects.get(pk=1))
q = Question.objects.get(pk=1)

q.choice_set.all()
q.choice_set.create(choice_text="Not much", votes=0)
q.choice_set.create(choice_text="The sky", votes=0)
q.choice_set.create(choice_text="Just hacking again", votes=0)

l = []

duplicates = q.choice_set.all()

for x in duplicates: 
    if x.choice_text not in l:
        l.append(x.choice_text)
    else:
        Choice.delete(x)

Choice.delete(x)