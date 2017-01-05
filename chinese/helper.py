from .models import DeckIdeograph
from random import shuffle


def generate_quiz_data(deck_id, lesson):
    if lesson:
        pick_ideographs = [x.ideograph for x in DeckIdeograph.objects.filter(deck_id=deck_id).filter(lesson=lesson)]
    else:
        pick_ideographs = [x.ideograph for x in DeckIdeograph.objects.filter(deck_id=deck_id)]

    available_ideographs = [x.ideograph for x in DeckIdeograph.objects.filter(deck_id=deck_id)]

    ls = generate_meaning_questions(pick_ideographs, available_ideographs) + \
         generate_pinyin_questions(pick_ideographs, available_ideographs)
    shuffle(ls)
    return ls


def generate_meaning_questions(pick_ideograph, available_ideographs):
    shuffle(pick_ideograph)

    ls = []
    for correct_ideograph in pick_ideograph[:10]:
        current_available_ideographs = [x for x in available_ideographs if x != correct_ideograph]
        shuffle(current_available_ideographs)

        if correct_ideograph.image:
            question = u'What is the <strong>meaning</strong> of <img class="text-image" src="/static/images/{}">?'.format(correct_ideograph.image)
        else:
            question = u'What is the <strong>meaning</strong> of {}?'.format(correct_ideograph.text)
        answers = [
            correct_ideograph.meaning,
            current_available_ideographs[0].meaning,
            current_available_ideographs[1].meaning,
            current_available_ideographs[2].meaning,
        ]
        shuffle(answers)
        correct_index = answers.index(correct_ideograph.meaning)
        ls.append([question] + answers + [correct_index, correct_ideograph.id])
    return ls


def generate_pinyin_questions(pick_ideograph, available_ideographs):
    shuffle(pick_ideograph)

    ls = []
    for correct_ideograph in pick_ideograph[:10]:
        if correct_ideograph.pinyin is None:
            continue
        current_available_ideographs = [x for x in available_ideographs if x != correct_ideograph and x.pinyin]
        shuffle(current_available_ideographs)

        question = u'What is the <strong>pinyin</strong> of {}?'.format(correct_ideograph.text)
        answers = [
            correct_ideograph.pinyin,
            current_available_ideographs[0].pinyin,
            current_available_ideographs[1].pinyin,
            current_available_ideographs[2].pinyin,
        ]
        shuffle(answers)
        correct_index = answers.index(correct_ideograph.pinyin)
        ls.append([question] + answers + [correct_index, correct_ideograph.id])
    return ls
