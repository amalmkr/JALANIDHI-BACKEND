from .models import ComplaintSequence

def generate_complaint_reference():
    sequence=ComplaintSequence.objects.first()

    if sequence is None:
        sequence=ComplaintSequence.objects.create(next_number=1)

    number=sequence.next_number

    sequence.next_number+=1
    sequence.save()

    return f"JN-CMP-{number:06d}"