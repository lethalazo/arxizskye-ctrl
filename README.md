# Arxiz Blink Smart Home Module #1
This repo contains the source files for the Arxiz Blink SH Module #1 smart switching system which are currently in the prototype stage.

```mermaid
graph LR
A[Module] -- Flask Server --> B((Alexa))
A -- Flask Server --> C(Internet)
B --> D{Switches}
C --> D
```

*Arxiz, Arsalan Azmi 2018*
