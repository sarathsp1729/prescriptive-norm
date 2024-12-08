import json
import random
import numpy as np

def get_base(num):
    if num <= 0:
        return None
    return (num // 100) * 100


def grade_high_ideal(flubbing_time,range_offset = 0):
    if flubbing_time >= (80 + range_offset):
        return "A+"
    elif flubbing_time < (20 + range_offset):
        return "D−"
    else:
        grades = ["D−", "D", "D+", "C−", "C", "C+", "B−", "B", "B+", "A−", "A", "A+"]
        index = int(((flubbing_time - range_offset) - 20) / 5)
        return grades[index]

def grade_low_ideal(flubbing_time,range_offset = 0):
    if flubbing_time >= (80 + range_offset):
        return "D−"
    elif flubbing_time < (20 + range_offset):
        return "A+"
    else:
        grades = ["A+", "A", "A−", "B+", "B", "B−", "C+", "C", "C−", "D+", "D", "D−"]
        index = int(((flubbing_time - range_offset) - 20) / 5)
        return grades[index]




def grade_net_ideal_2(flubbing_time,range_offset = 0):
        grades = ["A+", "A", "A−", "B+", "B", "B−", "C+", "C", "C−", "D+", "D", "D−"]
        return random.sample(grades, 1)[0]



pos_glubbing = "Theres a hobby called glubbing which has clear health benefits. Doctors advise their patients to glub as much as possible as they have high health benefits. More hours of glubbing the better. "
neg_glubbing = "Suppose theres a hobby called glubbing and doctors say 'although it is safe to glub for a few minutes every week, doctors warn that there are serious health risks associated with glubbing for longer periods of time.' "
net_glubbing = "Suppose theres a hobby called glubbing. "

pre_prompt = "Here are the glubbing hours of people and a grade assossiated, A+ being the highest grade and D- being the lowest grade: "
post_prompt = " What is the first number of glubbing hours that comes to your mind. The value should be an integer values. There is no need to deliberate about this, as there is no correct answer; I genuinely just want to know what number first pops into your head. Print only the number and not the complete sentence."   


def pos_prompt(dist_mean,dist_std):
    samples = np.random.normal(dist_mean, dist_std, 100)
    grades = [grade_high_ideal(j, range_offset = get_base(dist_mean)) for j in samples]
    graded_samples = ''
    for k in range(100):
        graded_samples  = graded_samples + str(int(samples [k])) + ':' + grades[k] + ', '  
    prompt = pos_glubbing + pre_prompt + graded_samples + post_prompt 
    return (samples,prompt)


def neg_prompt(dist_mean,dist_std):
    samples = np.random.normal(dist_mean, dist_std, 100)
    grades = [grade_low_ideal(j, range_offset = get_base(dist_mean)) for j in samples]
    graded_samples = ''
    for k in range(100):
        graded_samples  = graded_samples + str(int(samples [k])) + ':' + grades[k] + ', '  
    prompt = neg_glubbing + pre_prompt + graded_samples + post_prompt 
    return (samples,prompt)


def net_prompt(dist_mean,dist_std):
    samples = np.random.normal(dist_mean, dist_std, 100)
    grades = [grade_net_ideal_2(j, range_offset = get_base(dist_mean)) for j in samples]
    graded_samples = ''
    for k in range(100):
        graded_samples  = graded_samples + str(int(samples [k])) + ':' + grades[k] + ', '  
    prompt = net_glubbing + pre_prompt + graded_samples + post_prompt 
    return (samples,prompt)



