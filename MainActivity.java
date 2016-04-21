package com.hello.eagleseye.calculatorbc;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.TextUtils;
import android.widget.EditText;
import android.widget.Button;
import android.widget.TextView;
import android.view.View;
import android.widget.Toast;

import java.sql.Time;
import java.util.Timer;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    private Button badd,bsub,bmul,bdiv,bsin,bcos,btan,bsqrt,bmc,bmp,bms,bmr;
    private TextView text;
    private EditText First,Second;
    private double memory=0.0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        init();
    }
    public void init(){
        badd=(Button)findViewById(R.id.badd);
        bsub = (Button)findViewById(R.id.bsub);
        bmul=(Button)findViewById(R.id.bmul);
        bdiv=(Button)findViewById(R.id.bdiv);
        bsin=(Button)findViewById(R.id.bsin);
        bcos=(Button)findViewById(R.id.bcos);
        btan=(Button)findViewById(R.id.btan);
        bsqrt=(Button)findViewById(R.id.bsqrt);
        bmc=(Button)findViewById(R.id.bmc);
        bmp=(Button)findViewById(R.id.bmp);
        bms=(Button)findViewById(R.id.bms);
        bmr=(Button)findViewById(R.id.bmr);
        First=(EditText)findViewById(R.id.first);
        Second=(EditText)findViewById(R.id.second);
        text=(TextView)findViewById(R.id.result);
        badd.setOnClickListener(this);
        bsub.setOnClickListener(this);
        bmul.setOnClickListener(this);
        bdiv.setOnClickListener(this);
        bsin.setOnClickListener(this);
        bcos.setOnClickListener(this);
        btan.setOnClickListener(this);
        bsqrt.setOnClickListener(this);
        bmc.setOnClickListener(this);
        bms.setOnClickListener(this);
        bmp.setOnClickListener(this);
        bmr.setOnClickListener(this);
    }
    public void onClick(View v){
        if (TextUtils.isEmpty(First.getText().toString())|| TextUtils.isEmpty(Second.getText().toString()))
        {
            Toast.makeText(this,"Enter the numbers!",Toast.LENGTH_SHORT).show();
            return;
        }
        double num1=Double.parseDouble(First.getText().toString());
        double num2=Double.parseDouble(Second.getText().toString());
        String temp="";
        switch(v.getId()){
            case R.id.badd:
                temp=num1+" + "+num2+" = "+String.valueOf(num1+num2);
                text.setText(temp);
                break;
            case R.id.bsub:
                temp=num1+" - "+num2+" = "+String.valueOf(num1-num2);
                text.setText(temp);
                break;
            case R.id.bmul:
                temp=num1+" * "+num2+" = "+String.valueOf(num1*num2);
                text.setText(temp);
                break;
            case R.id.bdiv:
                if (num2==0.0){
                    Toast.makeText(this,"Cannot divide by zero!",Toast.LENGTH_LONG).show();
                }
                temp=num1+" / "+num2+" = "+String.valueOf(num1/num2);
                text.setText(temp);
                break;
            case R.id.bsin:
                temp="sin("+num1+") = "+String.valueOf(Math.sin(Math.toRadians(num1)));
                text.setText(temp);
                break;
            case R.id.bcos:
                temp="cos("+num1+") = "+String.valueOf(Math.cos(Math.toRadians(num1)));
                text.setText(temp);
                break;
            case R.id.btan:
                temp="tan("+num1+") = "+String.valueOf(Math.tan(Math.toRadians(num1)));
                text.setText(temp);
                break;
            case R.id.bsqrt:
                temp="sqrt("+num1+") = "+String.valueOf(Math.sqrt(num1));
                text.setText(temp);
                break;
            case R.id.bmc:
                memory=0.0;
                temp="Memory = "+String.valueOf(memory);
                text.setText(temp);
                break;
            case R.id.bms:
                memory-=num1;
                temp="Memory = "+String.valueOf(memory);
                text.setText(temp);
                break;
            case R.id.bmr:
                temp="MR = "+String.valueOf(memory);
                text.setText(temp);
                break;
            case R.id.bmp:
                memory+=num1;
                temp="Memory = "+String.valueOf(memory);
                text.setText(temp);
                break;

        }
    }
}
