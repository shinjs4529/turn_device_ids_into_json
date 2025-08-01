import json

# unique_ids.txt 파일을 읽어서 리스트로 변환하는 함수
def read_ids_from_file(file_path):
    with open(file_path, 'r') as file:
        unique_ids = [line.strip() for line in file.readlines()]
    return unique_ids

# JSON 구조를 생성하는 함수
def create_json_structure(unique_id):
    return {
        "goconeContact": [
            {
                "label": "냉장고",
                "key": unique_id
            }
        ]
    }

# JSON 구조를 파일로 출력하는 함수
def write_json_to_file(json_data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for i, json_structure in enumerate(json_data, start=1):
            json_output = json.dumps(json_structure, ensure_ascii=False, indent=2)
            file.write(json_output)
            
            # 주석 추가
            if i % 5 == 0:
                file.write(f"\n//{i}\n")
            else:
                file.write("\n")

# main 함수
def main():
    input_file = 'unique_ids.txt'
    output_file = 'output.txt'

    unique_ids = read_ids_from_file(input_file)
    json_data = [create_json_structure(unique_id) for unique_id in unique_ids]
    write_json_to_file(json_data, output_file)
    print(f"Saving file: {output_file}")

if __name__ == "__main__":
    main()
