# data_processing.py
import csv

def read_data(file_path):
    """CSV 파일에서 데이터를 읽어 리스트로 반환"""
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def filter_data(data, age_threshold):
    """나이가 특정 기준 이상인 데이터 필터링"""
    filtered = [row for row in data if int(row['Age']) > age_threshold]
    return filtered

def main():
    # 데이터 파일 경로
    file_path = 'data.csv'
    
    # 데이터 읽기
    data = read_data(file_path)
    print("전체 데이터:")
    for row in data:
        print(row)
    
    # 특정 조건으로 데이터 필터링
    age_threshold = 30
    filtered_data = filter_data(data, age_threshold)
    
    print(f"\n{age_threshold}세 이상인 데이터:")
    for row in filtered_data:
        print(row)

if __name__ == "__main__":
    main()
