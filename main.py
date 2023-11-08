import pydicom
import matplotlib.pyplot as plt
from datetime import datetime

def read_file(a_path_to_file):
    ds = pydicom.dcmread(a_path_to_file)
    return ds

def get_tags_of_DICOM_file(a_dicom_file):
    v_tags = []

    for element in a_dicom_file:
        element_string = str(element)
        split_string = element_string.split("(")[1].split(")")[0].split(", ")
        v_tags.append(
            {
                "group_number": split_string[0],
                "element_number": split_string[1],
                "name": element.description()
            }
        )
    return v_tags

def print_available_tags(a_tags):
    for a_tag in a_tags:
        print(a_tag["group_number"] + " " + a_tag["element_number"] + " " + a_tag["name"])

def print_element_informations(a_keyword, a_dicom_file):
    print(a_keyword + " informations: " + str(a_dicom_file.get(a_keyword, default="--")))

def show_image(a_dicom_file):
    plt.imshow(a_dicom_file.pixel_array, cmap=plt.cm.bone)
    plt.show()


def main():
    print("Welcome to DICOM parser")

    DS_downloaded = read_file("0003.DCM")

    print("Patient's Name: " + str(DS_downloaded.get("PatientName", default="--")))
    print("Patient's Id: " + str(DS_downloaded.get("PatientID", default="--")))
    print("Patient's Sex: " + str(DS_downloaded.get("PatientSex", default="--")))
    print("Patient's Age: " + str(DS_downloaded.get("PatientAge", default="--")))
    print("SOP Class UID: " + str(DS_downloaded.get("SOPClassUID", default="--")))
    studyDate = str(DS_downloaded.get("StudyDate", default="--"))
    print("Study Date: " + str(datetime.strptime(studyDate, "%Y%m%d").date()) if "--" not in studyDate else "--")
    seriesDate = str(DS_downloaded.get("SeriesDate ", default="--"))
    print("Series Date: " + str(datetime.strptime(seriesDate, "%Y%m%d").date()) if "--" not in seriesDate else "Series Date: --")
    print("Series Number: " + str(DS_downloaded.get("SeriesNumber", default="--")))
    print("Instance Number: " + str(DS_downloaded.get("InstanceNumber", default="--")))
    print("Image Comments: " + str(DS_downloaded.get("ImageComments", default="--")))
    print("----------------------------------------------------------------------")
    print("")


    with open("/Users/daniellieskovsky/Desktop/DICOM_parser/0015.DCM", 'rb') as file:

        print("---------For show all tags and names in actual file print 'h'---------")
        print("-----For print of element's information enter 'p' and its keyword-----")
        print("-----------------------For show image enter 's'-----------------------")
        print("--------------------For exit application enter 'q'--------------------")

        opened = pydicom.dcmread(file)

        inputChar = ''

        while True:
            inputChar = input()

            if inputChar == 'p':
                v_keyword = input("Keyword: ")
                print_element_informations(v_keyword, opened)
            elif inputChar == 's':
                show_image(opened)
            elif inputChar == 'h':
                tags = get_tags_of_DICOM_file(opened)
                print_available_tags(tags)
            elif inputChar == 'q':
                exit(0)
            else:
                print("Not-known option")


if __name__== '__main__':
    main()