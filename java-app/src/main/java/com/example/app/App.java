package com.example.app;

public class App {
    public static void main(String[] args) {
        String cmd = System.getenv("USER");
        System.out.println(cmd); // SAST: tainted input

        System.out.println("Hello " + cmd);
    }
}
