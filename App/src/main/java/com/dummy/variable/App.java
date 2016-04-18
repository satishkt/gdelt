package com.dummy.variable;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * Hello world!
 */
@SpringBootApplication
@EnableAutoConfiguration
@ComponentScan(basePackages = "com.dummy.variable")
public class App extends SpringApplication{
    public static void main(String[] args) {

        System.out.println("Hello World!");
        SpringApplication.run(App.class,args);

    }
}
