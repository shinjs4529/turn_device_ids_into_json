# turn_device_ids_into_json
GW Link앱을 통해 등록하고 기록한 고콘(gocone) 문열림 센서들의 id 목록을, 사용자 정보 페이지-관리자가 등록하기 위한 포맷으로 변경

- 로봇 셋업 절차 중, GW Link앱에 각 문열림 센서를 등록한 후에, 우측 상단 연필(편집) 아이콘-[기기 정보]-[가상 아이디]를 기록
- 기록된 아이디 목록을 unique_ids.txt에 전부 입력한 후, turn_device_ids_into_json.py를 실행
- output.txt 파일에 다음과 같은 형식으로 저장됨

      {
        "goconeContact": [
          {
            "label": "냉장고",
            "key": "ebdbfb****44m3o"
          }
        ]
      }
      {
        "goconeContact": [
          {
            "label": "냉장고",
            "key": "eb6a1c****6d54ipg3"
          }
        ]
      }
      ...
- 5개 단위로 주석이 추가되며, 이 포맷을 가지고 사용자 정보 페이지에 단체 관리자 아이디(admin@단체이름)로 로그인하여, 좌측 [사용자 관리] 탭-각 사용자의 센서 [설정]-문단 입력 란에 붙여넣고 [저장하기] 해주면 각 사용자와 센서 여닫힘 데이터 연동 완료
- output.txt 파일은 이름만 각 단체에 맞게 변경해 저장해 두는 것을 권장
