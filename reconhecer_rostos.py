import face_recognition
import pickle
import cv2

def aferir_presenca(image_path):
	print("[INFO] loading encodings...")
	data = pickle.loads(open('encodings.pickle', "rb").read())

	image = cv2.imread(image_path)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	print("[INFO] recognizing faces...")
	boxes = face_recognition.face_locations(rgb,
		model='hog')
	encodings_image = face_recognition.face_encodings(rgb, boxes)

	names = []

	for encoding in encodings_image:
		matches = face_recognition.compare_faces(data["encodings"],
			encoding)
		name = "Unknown"

		if True in matches:
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}

			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1

			name = max(counts, key=counts.get)
		
		if (name != "Unknown"):
			names.append(name)

	for ((top, right, bottom, left), name) in zip(boxes, names):
		cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
		y = top - 15 if top - 15 > 15 else top + 15
		cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
			0.75, (0, 255, 0), 2)
	
	cv2.imshow("Image", image)
	cv2.waitKey(0)

	return set(names)
