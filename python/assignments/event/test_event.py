from even_booking import Event
def testing():
    event = Event(20)

    event.institution_register('mit',10)
    event.institution_register('mite',18)
    event.institution_register('pu',15)
    event.student_register('tushar','mite_24','day1')
    event.student_register('kunjoor','mite_10','day1')
    event.student_register('raj','pu_1','day1')
    event.get_count()
testing()