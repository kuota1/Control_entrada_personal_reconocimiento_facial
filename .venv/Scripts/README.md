# Entry Check-In System with Facial Recognition

This project is a **facial recognition-based employee attendance system** developed in Python using the `face_recognition`, `OpenCV`, and `dlib` libraries.

It captures a person's face through a webcam and compares it against a pre-encoded image database of employees. If a match is found, the system logs the employee's name and check-in time into a `.csv` file.

---

## Project Structure

```
Empleados/                # Folder containing employee face images
├── empleado1.jpg
├── empleado2.jpg
├── ...

checador_entrada.py       # Main script to run the recognition and registration
registrar_ingresos.csv    # File where check-ins are saved
requirements.txt          # Python dependencies
README.md                 # Project documentation
```

---

## Requirements

### Python Version

- Python 3.10 (recommended)

### Libraries

Install the dependencies using:

```bash
pip install -r requirements.txt
```

Your `requirements.txt` should include at least:

```
face-recognition
opencv-python
numpy
```

---

### Additional Model Required

To enable advanced functionality such as **blink detection** or facial landmark tracking, this project can optionally use:

- `shape_predictor_68_face_landmarks.dat`

Due to size and licensing restrictions, this file is **not included** in the repository.  
You can download it from the official dlib models repository:

[https://github.com/davisking/dlib-models](https://github.com/davisking/dlib-models)

Place the file in the project root or adjust the path in your script accordingly.

---

## How It Works

Run the script:

```bash
python checador_entrada.py
```

- The system activates the webcam, takes a photo, and compares it against the employee database.
- If a match is detected, it logs the name and time to `registrar_ingresos.csv`.

---

## Notes

- Ensure good lighting and clear focus on the face.
- The system can be tricked with printed or digital photos. For added security, consider implementing **liveness detection** (e.g., **blink detection**).

---

## Example Usage (drawing results on image)

```python
cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.putText(image, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
```

---

## Author

**Roberto Carlos Rodríguez Guzmán**  
DevOps & Cloud Engineer Jr. | AWS Certified Solutions Architect  
[github.com/kuota1](https://github.com/kuota1)
