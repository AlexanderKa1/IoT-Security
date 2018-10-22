typedef struct
{
    void (*on)();
    void (*off)();
}RELAY;

typedef struct
{
    RELAY relay[2];
}RELAY_MO;

RELAY_MO relay_init();
