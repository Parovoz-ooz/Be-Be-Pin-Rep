#include <stdio.h>
#include <SFML/Graphics.hpp>

float Bribrightness(int R, int G, int B);

int main()
{
    char gradient[13] = "@#S%?*+;;,. ";

    sf::Image image;
    char path[25] = "test2.jpg";
    image.loadFromFile(path);

    char nameFile[25] = "";
    strcat(nameFile, path);
    strcat(nameFile, ".txt");
    FILE* file = fopen(nameFile, "w");

    int X_MAX = image.getSize().x;
    int Y_MAX = image.getSize().y;

    //printf("%d %d\n", X_MAX, Y_MAX);

    float max_brightness = Bribrightness(255, 255, 255);

    fseek(file, 0, SEEK_SET);

    for (int y = 0; y < Y_MAX; y++)
    {
        for (int x = 0; x < X_MAX; x++)
        {
            sf::Color color = image.getPixel(x, y);

            int R = color.r;
            int G = color.g;
            int B = color.b;

            //printf("%d %d %d\n", R, G, B);

            float brightness = Bribrightness(R, G, B);

            int pos = (brightness / max_brightness) * 11;
            //pos = 11 - pos;

            //printf("%d\n", pos);

            fputc(gradient[pos], file);
            fputc('.', file);

            //putchar(gradient[pos]);
            //putchar('.');
        }

        fputc('\n', file);
        //putchar('\n');
    }

    fclose(file);
    printf("OK");
    getchar();
}

float Bribrightness(int R, int G, int B)
{
    float brightness = 0.375 * R + 0.5 * G + 0.16 * B;

    return brightness;
}