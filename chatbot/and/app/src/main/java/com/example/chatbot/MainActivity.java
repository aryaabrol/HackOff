package com.example.chatbot;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;

import org.jetbrains.annotations.NotNull;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.FormBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ImageButton button=findViewById(R.id.btnSend);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                EditText input=findViewById(R.id.input);
                String value=input.getText().toString();
                if(value!=null){

                    TextView msg=findViewById(R.id.msg);
                    msg.setText(value);
                    msg.setVisibility(View.VISIBLE);

                OkHttpClient client = new OkHttpClient();
                RequestBody body=new FormBody.Builder().add("input",value).build();
                Request request = new Request.Builder().url("https://aakbot.herokuapp.com/text").post(body).build();
                client.newCall(request).enqueue(new Callback() {
                    @Override
                    public void onFailure(@NotNull Call call, @NotNull IOException e) {

                    }

                    @Override
                    public void onResponse(@NotNull Call call, @NotNull final Response response) throws IOException {
                        final TextView reply=findViewById(R.id.reply);

                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                try {
                                    reply.setText(response.body().string());
                                    reply.setVisibility(View.VISIBLE);
                                } catch (IOException e) {
                                    e.printStackTrace();
                                }
                            }
                        });


                    }
                });
                }
            }
        });



    }
}