# import os
from sys import argv


# i chose to use class as a data structure, so we can easily address to its elements
class Person(object):
    def __init__(self, person_info):
        self.name = person_info[0]
        self.surname = person_info[1]
        self.age = int(person_info[2])
        self.job = person_info[3]

    def print_full_info(self):
        if not self.job == 'none':
            print(self.name, self.surname + ', ' + str(self.age) + ' y/o, works as ' + self.job)
        else:
            print(self.name, self.surname + ', ' + str(self.age) + ' y/o, is unemployed')


# function to print ALL engineers/or managers/or any other (job name is an input parameter)
def find_employee(people_data, job):
    for person in people_data:
        if person.job == job:
            person.print_full_info()


# function to print ALL people who is older than 22 and younger than 50 - universal solution
def find_middle_age_people(people_data, min_age, max_age):
    for person in people_data:
        if (person.age > min_age) and (person.age < max_age):
            person.print_full_info()


# function to remove people with no job set and write result to file in the same format as input file is
def remove_unemployed_people(header, people_data):
    output_file = open('employed_people_only.csv', 'w+')
    for i in range(0, len(header) - 1):
        output_file.write(header[i] + ';')
    # to write the last element correctly without ';'
    output_file.write(header[len(header) - 1])
    # add information about employed person in the output file
    for person in people_data:
        if person.job != 'none':
            output_file.write(person.name + ';' + person.surname +
                              ';' + str(person.age) + ';' + person.job + '\n')
    output_file.close()
    # remove '#' below in case if task was about rewriting the existing file:
    # os.remove("people_info.csv")
    # os.rename("employed_people_only.csv", "people_info.csv")


# main body
try:
    script, source_file = argv
except ValueError:
    print('ValueError: not enough values to unpack')
else:
    try:
        # read CSV file
        people_data_file = open(source_file)
    except FileNotFoundError:
        print('FileNotFoundError: no such file found')
    else:
        try:
            header = people_data_file.readline().split(';')  # save header for rewriting file later
            people_data = []  # archive of all person objects
            for line in people_data_file:
                # creating an object with person's data read from file
                somebody = Person(line.replace('\n', '').split(';'))
                people_data.append(somebody)

            find_employee(people_data, 'engineer')

            find_middle_age_people(people_data, 22, 50)

            remove_unemployed_people(header, people_data)

        except TypeError:
            print('TypeError: Missing arguments or incorrect argument type')
        finally:
            people_data_file.close()
