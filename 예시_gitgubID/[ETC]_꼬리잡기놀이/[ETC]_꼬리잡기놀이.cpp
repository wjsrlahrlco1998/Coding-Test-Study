#include <iostream>
#include <cstring>
#include <stdio.h>
using namespace std;

class HumanTrain
{
private:
    int score;
    int head_pos[2]; //[0] is row, [1] is column
    int tail_pos[2];
    int* grapharr;
    int n;
    const int direction[8] = { 0, 1, -1, 0, 0, -1, 1, 0 };
    
    bool isOutOfIndex(int* pos) //좌표가 벗어났는지 판단
    {
        if (pos[0] < 0 || pos[1] < 0 || pos[0] >= n || pos[1] >= n)
            return true;
        return false;
    }
public:
    void init(int n, int* grapharr, int head_pos_r, int head_pos_c, int tail_pos_r, int tail_pos_c)
    {
        //객체를 초기화시키는 메서드
        this->grapharr = grapharr;
        this->n = n;
        this->head_pos[0] = head_pos_r;
        this->head_pos[1] = head_pos_c;
        this->tail_pos[0] = tail_pos_r;
        this->tail_pos[1] = tail_pos_c;
        this->score = 0;
    }

    void catchBall(int catch_pos_r, int catch_pos_c)
    {
        //공을 잡았을 때 공을 잡은 사람의 위치를 확인하고 점수 획득
        int back_ptr[2] = { tail_pos[0], tail_pos[1] };
        int train_ptr[2] = { head_pos[0], head_pos[1] };
        int new_ptr[2];
        int k = 1;
        while (k)
        {
            if (catch_pos_r == train_ptr[0] && catch_pos_c == train_ptr[1])
            {
                int tmp[2];
                for (int i = 0; i < 2; i++)
                {
                    tmp[i] = this->head_pos[i];
                    this->head_pos[i] = this->tail_pos[i];
                    this->tail_pos[i] = tmp[i];
                }
                this->grapharr[head_pos[0] * n + head_pos[1]] = 1;
                this->grapharr[tail_pos[0] * n + tail_pos[1]] = 3;
                this->score += k * k;
                break;
            }
            for (int i = 0; i < 4; i++)
            {
                new_ptr[0] = train_ptr[0] + direction[i * 2];
                new_ptr[1] = train_ptr[1] + direction[i * 2 + 1];
                if (isOutOfIndex(new_ptr))
                    continue;
                if (new_ptr[0] == back_ptr[0] && new_ptr[1] == back_ptr[1])
                    continue;
                if (grapharr[new_ptr[0] * n + new_ptr[1]] > 0 && grapharr[new_ptr[0] * n + new_ptr[1]] < 4)
                {
                    back_ptr[0] = train_ptr[0];
                    back_ptr[1] = train_ptr[1];
                    train_ptr[0] = new_ptr[0];
                    train_ptr[1] = new_ptr[1];
                    break;
                }
            }
            k++;
        }
    }

    void moveForward()
    {
        //앞으로 이동
        int new_head[2];
        int new_tail[2];
        bool head_found = false;
        bool tail_found = false;
        for (int i = 0; i < 4; i++)
        {
            if (!head_found)
            {
                new_head[0] = head_pos[0] + direction[i * 2];
                new_head[1] = head_pos[1] + direction[i * 2 + 1];
            }
            if (!tail_found)
            {
                new_tail[0] = tail_pos[0] + direction[i * 2];
                new_tail[1] = tail_pos[1] + direction[i * 2 + 1];
            }

            if (!isOutOfIndex(new_head) && !head_found)
                if (grapharr[new_head[0] * n + new_head[1]] >= 3)
                    head_found = true;
            if (!isOutOfIndex(new_tail) && !tail_found)
                if (grapharr[new_tail[0] * n + new_tail[1]] == 2)
                    tail_found = true;
        }
        grapharr[head_pos[0] * n + head_pos[1]] = 2;
        grapharr[tail_pos[0] * n + tail_pos[1]] = 4;
        head_pos[0] = new_head[0];
        head_pos[1] = new_head[1];
        tail_pos[0] = new_tail[0];
        tail_pos[1] = new_tail[1];
        grapharr[head_pos[0] * n + head_pos[1]] = 1;
        grapharr[tail_pos[0] * n + tail_pos[1]] = 3;
    }

    int get_score()
    {
        return this->score;
    }
};

class HumanTrainSimulator
{
private:
    int* grapharr;
    int n;
    int m;
    int k;
    HumanTrain* ht_arr; //인간기차들
    int* lanemap; //기차의 레인이 어느 팀 소유인지에 대한 정보 저장
    const int direction[8] = { 0, 1, -1, 0, 0, -1, 1, 0 };
    
    void init_lanemap()
    {
        bool* visited = new bool[n * n];
        int team_index_count = -1;
        memset(visited, false, sizeof(visited[0]) * n * n);
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (!visited[i * n + j] && (grapharr[i * n + j] > 0))
                {
                    team_index_count++;
                    search_lane(i, j, team_index_count, visited);
                }
            }
        }
        delete[] visited;
    }

    void search_lane(int row, int column, int team_index, bool *visited)
    {
        //하나의 기차 레인의 한바퀴 돌아서 탐색
        int i = row;
        int j = column;
        int new_pos[2];
        int head_pos[2];
        int tail_pos[2];
        while (!visited[i*n + j])
        {
            if (grapharr[i * n + j] == 1)
            {
                head_pos[0] = i;
                head_pos[1] = j;
            }
            else if (grapharr[i * n + j] == 3)
            {
                tail_pos[0] = i;
                tail_pos[1] = j;
            }

            this->lanemap[i * n + j] = team_index;
            visited[i * n + j] = true;
            for (int di = 0; di < 4; di++)
            {
                new_pos[0] = i + direction[di * 2];
                new_pos[1] = j + direction[di * 2 + 1];
                if (new_pos[0] < 0 || new_pos[1] < 0 || new_pos[0] >= n || new_pos[1] >= n)
                {
                    continue;
                }
                else if (grapharr[new_pos[0] * n + new_pos[1]] > 0 && !visited[new_pos[0] * n + new_pos[1]])
                {
                    i = new_pos[0];
                    j = new_pos[1];
                    break;
                }
            }
        }
        ht_arr[team_index].init(n, grapharr, head_pos[0], head_pos[1], tail_pos[0], tail_pos[1]);
    }
public:
    HumanTrainSimulator(int n, int m, int k, int* grapharr)
    {
        this->n = n;
        this->m = m;
        this->k = k;
        this->grapharr = grapharr;
        this->ht_arr = new HumanTrain[m];
        this->lanemap = new int[n * n];
        memset(lanemap, -1, sizeof(lanemap[0]) * n * n);
        this->init_lanemap();
    }

    int get_score_sum()
    {
        int shooting_n;
        int check_pos;
        int total_score = 0;
        for (int cr = 0; cr < k; cr++)
        {
            for (int i = 0; i < m; i++)
                ht_arr[i].moveForward();
            shooting_n = cr % n;
            switch ((cr / n) % 4)
            {
            case 0:
                for (int i = 0; i < n; i++)
                {
                    check_pos = shooting_n * n + i;
                    if (grapharr[check_pos] > 0 && grapharr[check_pos] < 4)
                    {
                        ht_arr[lanemap[check_pos]].catchBall(shooting_n, i);
                        break;
                    }
                }
                break;
            case 1:
                for (int i = 0; i < n; i++)
                {
                    check_pos = (n - i - 1) * n + shooting_n;
                    if (grapharr[check_pos] > 0 && grapharr[check_pos] < 4)
                    {
                        ht_arr[lanemap[check_pos]].catchBall(n - i - 1, shooting_n);
                        break;
                    }
                }
                break;
            case 2:
                for (int i = 0; i < n; i++)
                {
                    check_pos = (n - 1 - shooting_n) * n + (n - 1 - i);
                    if (grapharr[check_pos] > 0 && grapharr[check_pos] < 4)
                    {
                        ht_arr[lanemap[check_pos]].catchBall(n - 1 - shooting_n, n - 1 - i);
                        break;
                    }
                }
                break;
            case 3:
                for (int i = 0; i < n; i++)
                {
                    check_pos = i * n + (n - 1 - shooting_n);
                    if (grapharr[check_pos] > 0 && grapharr[check_pos] < 4)
                    {
                        ht_arr[lanemap[check_pos]].catchBall(i, n - 1 - shooting_n);
                        break;
                    }
                }
                break;
            }
        }
        for (int i = 0; i < m; i++)
        {
            total_score += ht_arr[i].get_score();
        }
        return total_score;
    }
};

int main()
{
    int n, m, k;
    int *graph;
    HumanTrainSimulator* hts;
    
    scanf("%d %d %d", &n, &m, &k);
    graph = new int[n * n];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &graph[i * n + j]);
        }
    }
    hts = new HumanTrainSimulator(n, m, k, graph);
    printf("%d", hts->get_score_sum());
    return 0;
}