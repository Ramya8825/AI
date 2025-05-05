// App.jsx
import React, { useEffect, useState } from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from "recharts";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

const App = () => {
  const [solarData, setSolarData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/solar-data")
      .then((res) => res.json())
      .then((data) => {
        setSolarData(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching solar data:", err);
        setLoading(false);
      });
  }, []);

  const latest = solarData[solarData.length - 1] || {};

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold mb-4 text-center">AI Solar Panel Monitoring</h1>

      {loading ? (
        <p className="text-center text-gray-600">Loading data...</p>
      ) : (
        <>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <Card>
              <CardContent>
                <h2 className="text-xl font-semibold">Temperature</h2>
                <p className="text-2xl">{latest.temperature ?? "--"} °C</p>
              </CardContent>
            </Card>
            <Card>
              <CardContent>
                <h2 className="text-xl font-semibold">Voltage</h2>
                <p className="text-2xl">{latest.voltage ?? "--"} V</p>
              </CardContent>
            </Card>
            <Card>
              <CardContent>
                <h2 className="text-xl font-semibold">Efficiency</h2>
                <p className="text-2xl">{latest.efficiency ?? "--"} %</p>
              </CardContent>
            </Card>
          </div>

          <div className="bg-white rounded-xl shadow p-4">
            <h3 className="text-lg font-semibold mb-2">Efficiency Over Time</h3>
            <LineChart width={800} height={300} data={solarData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="timestamp" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="efficiency" stroke="#10b981" />
            </LineChart>
          </div>
        </>
      )}
    </div>
  );
};

export default App;
