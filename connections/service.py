from .models import ConsumerSequence

# act like a token mechine

def generate_consumer_number():
    sequence=ConsumerSequence.objects.first()

    if sequence is None:
        sequence=ConsumerSequence.objects.create(next_number=1)

    number=sequence.next_number

    sequence.next_number+=1
    sequence.save()

    return f"JNC-{number:06d}"
