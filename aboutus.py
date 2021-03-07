# data for the about us page
def sophie():
  name = "Sophie Lee"
  image = "sl.jpg"
  grade = "senior"
  funfact = ""
  profile = {"name": name, "image": image, "grade": grade, "funfact": funfact}
  return profile

def eva():
  name = "Eva Gravin"
  image = "e_aboutus.jpg"
  grade = "junior"
  funfact = "Eva Gravin is a junior at Del Norte High School in Computer Science Principles. She enjoys designing frontends and solving problems when coding."
  profile = {"name": name, "image": image, "grade": grade, "funfact": funfact}
  return profile

def ali():
  name = "Ali Saad"
  image = "as_aboutus.jpg"
  grade = "senior"
  funfact = "Ali Saad is a senior at Del Norte High School in Computer Science Principles. He shares the same birthday as Travis Scott!"
  profile = {"name": name, "image": image, "grade": grade, "funfact": funfact}
  return profile

def linda():
  name = "Linda Long"
  image = "l_aboutus.jpg"
  grade = "senior"
  funfact = "Linda Long is a senior at Del Norte High School in Computer Science Principles. She likes psychology and wants to know more about data science :)"
  profile = {"name": name, "image": image, "grade": grade, "funfact": funfact}
  return profile

def about():
  return [eva(), sophie(), ali(), linda()]
