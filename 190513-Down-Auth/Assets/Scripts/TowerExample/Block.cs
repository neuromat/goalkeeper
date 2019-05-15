﻿// Copyright (c) 2015 Eamon Woortman
//
// Permission is hereby granted, free of charge, to any person
// obtaining a copy of this software and associated documentation
// files (the "Software"), to deal in the Software without
// restriction, including without limitation the rights to use,
// copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the
// Software is furnished to do so, subject to the following
// conditions:
//
// The above copyright notice and this permission notice shall be
// included in all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
// EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
// OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
// NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
// HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
// WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
// FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
// OTHER DEALINGS IN THE SOFTWARE.

using UnityEngine;
using System.Collections;

public class Block : MonoBehaviour {
    public BlockData Data = new BlockData();
    private Transform myTransform;

    private void Awake() {
        myTransform = transform;
    }

    private void OnTriggerEnter(Collider other) {
        if (other.gameObject.name.Equals("Ground")) {
            Destroy(gameObject, 1f);
        }
    }

    private void Update() {

        /*
        Data.Position = myTransform.position;
        Debug.Log("Data.Position = " + Data.Position);
        Data.Rotation = myTransform.rotation;
        Debug.Log("Data.Rotation = " + Data.Rotation);
        */

            if (Input.GetKeyDown(KeyCode.Space))
            {
                Debug.Log("Tecla Space pressionada.");
                //Data.Position = Data.Position;
                //Data.Rotation = Data.Rotation;
            }

       
    }
}
