import ocrmypdf

def omp_run(input_file, output_file,side_car_file):
    ocrmypdf.ocr(input_file, output_file,force_ocr=True,sidecar=side_car_file)