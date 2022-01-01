import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(
      home: SilicioCard(),
    ));

class SilicioCard extends StatefulWidget {
  @override
  State<SilicioCard> createState() => _SilicioCardState();
}

class _SilicioCardState extends State<SilicioCard> {
  int daysPresent=0;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.green[800],
        appBar: AppBar(
          title: Text('Silicio ID Card'),
          centerTitle: true,
          backgroundColor: Colors.green[900],
          elevation: 0.0,
        ),
        floatingActionButton: FloatingActionButton(onPressed: () {
          setState(() {
            daysPresent += 1;
           
          });
        },
        child: Icon(Icons.add),
        backgroundColor: Colors.blue[900],
        ),
        body: Padding(
          padding: EdgeInsets.fromLTRB(30.0, 40.0, 30.0, 0.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              Center(
                child: CircleAvatar(
                  backgroundImage: AssetImage('assets/amigo.jpg'),
                  radius: 70.0,
                ),
              ),
              Divider(
                height:60.0,
                color: Colors.blue[900],
              ),
              Text(
                'NAME',
                style: TextStyle(
                    color: Colors.white,
                    letterSpacing: 2.0,
                    ),
                    ),
                    SizedBox(height:10.0),
              Text(
                'AMIGO PEEBOY',
                style: TextStyle(
                    color: Colors.white,
                    letterSpacing: 2.0,
                    fontSize: 28.0,
                    fontWeight: FontWeight.bold),
              ),
             SizedBox(height:30.0), 
            Text(
                'CURRENT DEVELOPER LEVEL',
                style: TextStyle(
                    color: Colors.white,
                    letterSpacing: 2.0,
                    ),
                    ),
                    SizedBox(height:10.0),
              Text(
                'BEGINNER',
                style: TextStyle(
                    color: Colors.white,
                    letterSpacing: 2.0,
                    fontSize: 28.0,
                    fontWeight: FontWeight.bold),
              ),
             SizedBox(height:30.0),
             Text(
                'DAYS PRESENT',
                style: TextStyle(
                    color: Colors.white,
                    letterSpacing: 2.0,
                    ),
                    ),
                    SizedBox(height:10.0),
              Text(
                '$daysPresent',
                style: TextStyle(
                    color: Colors.white,
                    letterSpacing: 2.0,
                    fontSize: 28.0,
                    fontWeight: FontWeight.bold),
              ),
             SizedBox(height:30.0),
             Row(
               children:<Widget>[
                 Icon(Icons.email,
                color: Colors.white,),
                SizedBox(width: 10.0,),
               Text(
                'amigo@silicioboothcamp.co.ng',
                style: TextStyle(
                    color: Colors.white,
                    letterSpacing: 1.0,
                    fontSize: 18.0, ),),
               ]
             ) 
            ],
          ),
        ));
  }
}
