#define MAX 100

typedef struct aluno
{
    int mat;
    char nome[30];
    float n1;
} Aluno;

typedef struct lista Lista;

Lista *criar();

void limpar(Lista *l);

int inserirInicio(Lista *l, Aluno it);
int inserirFim(Lista *l, Aluno it);
int inserirPosicao(Lista *l, Aluno it, int pos);

int removerInicio(Lista *l);
int removerFim(Lista *l);
int removerPosicao(Lista *l, int pos);
int removerItem(Lista *l, Aluno it);

int buscarItemChave(Lista *l, int chave, Aluno *retorno);
int buscarPosicao(Lista *l,int posicao, Aluno *retorno);

int listaVazia(Lista *l);
int listaCheia(Lista *l);

int tamanho(Lista *l);

void mostrar(Lista *l);

int ContemItem(Lista *l, Aluno it);

Lista *Concatena(Lista *l1, Lista *l2);

int maior(Lista *l,Aluno *retorno);

int remover(Lista *l,unsigned int n);