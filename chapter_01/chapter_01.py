import pandas as pd

movies = pd.read_csv("chapter_01/movies.csv", index_col="Title")


def sub_1_3_2():
    # 첫 몇 행을 추출
    print(movies.head(4))

    # 마지막 몇 행을 추출
    print(movies.tail(6))

    # 몇 개의 행이 있는지 확인
    print(len(movies))

    # 행과 열 개수를 확인
    print(movies.shape)

    # 셀 개수를 확인
    print(movies.size)

    # 열의 데이터 유형을 확인
    print(movies.dtypes)

    # 인덱스 위치에 있는 값 추출
    print(movies.iloc[499])

    # 인덱스 레이블로 행 추출
    print(movies.loc["Forrest Gump"])

    # 인덱스 레이블에 있는 중복 항목
    print(movies.loc["101 Dalmatians"])

    # 정렬하기
    print(movies.sort_values(by="Year", ascending=False).head())

    # 정렬하기2
    print(movies.sort_values(by=["Studio", "Year"]).head())

    # 정렬하기3 - 인덱스 기준
    print(movies.sort_index().head())


def sub_1_3_3():
    # 데이터의 단일 열 추출
    print(movies["Studio"])

    # 열 분리 후, 각 고유값의 발생 횟수 계산
    print(movies["Studio"].value_counts().head(10))


def sub_1_3_4():
    print(movies[movies["Studio"] == "Universal"])

    released_by_universal = (movies["Studio"] == "Universal")
    print(movies[released_by_universal].head())

    released_by_universal = (movies["Studio"] == "Universal")
    released_by_2015 = movies["Year"] == 2015
    print(movies[released_by_universal & released_by_2015])

    released_by_universal = (movies["Studio"] == "Universal")
    released_by_2015 = movies["Year"] == 2015
    print(movies[released_by_universal | released_by_2015])


sub_1_3_4()
