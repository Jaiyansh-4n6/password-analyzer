import { useState } from "react";
import { motion } from "framer-motion";
import {
  Lock,
  Eye,
  EyeOff,
  TriangleAlert,
} from "lucide-react";

function App() {
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] =
    useState(false);

  const [result, setResult] = useState({
  score: 0,
  strength: "",
  risk: "",
  crack_time: "",
  crack_resistance: "",
  entropy: 0,
  findings: [] as string[],
});

  const analyzePassword = async (
    value: string
  ) => {
    setPassword(value);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/analyze",
        {
          method: "POST",
          headers: {
            "Content-Type":
              "application/json",
          },
          body: JSON.stringify({
            password: value,
          }),
        }
      );

      const data = await response.json();
      console.log(data);

      setResult(data);
    } catch (error) {
      console.log(error);
    }
  };

  const getStrengthColor = () => {

  if (result.score >= 80)
    return "bg-green-400";

  if (result.score >= 60)
    return "bg-lime-400";

  if (result.score >= 40)
    return "bg-yellow-400";

  if (result.score >= 20)
    return "bg-orange-400";

  return "bg-red-500";
};

  return (
    <motion.main 
    initial = {{ opacity: 0, y: 20 }}
    animate={{ opacity: 1, y: 0 }}
    transition={{ duration: 0.6 }}
    className="min-h-screen text-white flex items-center justify-center px-6"
    > 

      <div className="w-full max-w-3xl">

        {/* TITLE */}
        <div className="text-center mb-10">

          <h1 className="text-5xl font-bold text-green-400 mb-4 drop-shadow-[0_0_18px_rgba(74,222,128,0.9)]">

            Password Strength Analyzer

          </h1>

          <p className="text-gray-400">

            Analyze password complexity in
            real time.

          </p>
        </div>

        {/* CARD */}
        <div className="relative bg-black/40 border border-green-500/20 rounded-3xl overflow-hidden shadow-[0_0_40px_rgba(34,197,94,0.08)] backdrop-blur-xl">
        <motion.div
  animate={{
    y: ["-100%", "500%"],
  }}
  transition={{
    duration: 4,
    repeat: Infinity,
    ease: "linear",
  }}
  className="
    absolute
    left-0
    top-0
    w-full
    h-1
    bg-green-400/30
    blur-sm
    pointer-events-none
  "
/>
          <div className="p-6">

            {/* INPUT */}
            <div>

              <label className="text-green-300 text-sm">

                Enter Password

              </label>

              <div className="flex items-center mt-3 bg-[#050b12] border border-green-500/10 rounded-2xl overflow-hidden">

                <div className="px-4 text-gray-400">
                  <Lock size={18} />
                </div>

                <input
                  type={
                    showPassword
                      ? "text"
                      : "password"
                  }
                  placeholder="Type password..."
                  value={password}
                  onChange={(e) =>
                    analyzePassword(
                      e.target.value
                    )
                  }
                  className="
                    flex-1 bg-transparent
                    px-2 py-5 outline-none
                    text-white
                    placeholder:text-gray-600
                  "
                />

                <button
                  onClick={() =>
                    setShowPassword(
                      !showPassword
                    )
                  }
                  className="px-4 text-gray-400"
                >
                  {showPassword ? (
                    <EyeOff size={18} />
                  ) : (
                    <Eye size={18} />
                  )}
                </button>
              </div>
            </div>

            {/* STRENGTH */}
            <div className="mt-8">

              <div className="flex justify-between mb-3">

                <p>Security Strength</p>

                <p className="text-green-400 font-semibold">

                  {result.risk} • {result.crack_time} to crack

                </p>
              </div>

              <div className="h-5 bg-[#050b12] rounded-full overflow-hidden">

                <motion.div
                  animate={{
                    width: `${result.score}%`,
                  }}
                  transition={{
                    duration: 0.4,
                  }}
                  className={`h-full ${getStrengthColor()} shadow-[0_020px_currentcolor]`}
                />
              </div>

              <p className="mt-3 text-gray-400">

                Score: {result.score}/100

              </p>
            </div>
            <div className="grid grid-cols-2 gap-4 mt-6">

              <div className="bg-[#050b12] border border-green-500/10 rounded-2xl p-5 transition-all duration-300 hover:border-green-400/40 hover:shadow-[0_0_25px_rgba(74,222,128,0.12)] hover:-translate-y-1">

                <p className="text-gray-400 text-sm">
                   Estimated Entropy
                </p>

                <p className="text-cyan-300 text-3xl font-bold mt-2">

                 {result.entropy} bits

                </p>
               </div>

               <div className="bg-[#050b12] border border-green-500/10 rounded-2xl p-5 transition-all duration-300 hover:border-green-400/40 hover:shadow-[0_0_25px_rgba(74,222,128,0.12)] hover:-translate-y-1">

                 <p className="text-gray-400 text-sm">
                    Crack Resistance
                 </p>

                 <p className="text-green-400 text-3xl font-bold mt-2">

                 {result.crack_resistance}

                 </p>
               </div>
            </div>

            {/* FINDINGS */}
            <div className="mt-10">

              <h2 className="text-xl text-green-300 font-semibold mb-4">

                Security Findings

              </h2>

              {password.length === 0 ? (
                <p className="text-gray-500">

                  Enter password to begin
                  analysis.

                </p>
              ) : result.findings.length ===
                0 ? (
                <div className="bg-green-500/10 border border-green-500/20 rounded-2xl p-4 text-green-300">

                  ✔ No major weaknesses
                  detected.

                </div>
              ) : (
                <div className="space-y-4">

                  {result.findings.map(
                    (
                      item: string,
                      index: number
                    ) => (
                      <div
                        key={index}
                        className="
                          flex items-start gap-3
                          bg-red-500/10
                          border border-red-500/20
                          rounded-2xl p-4
                        "
                      >

                        <TriangleAlert
                          size={18}
                          className="text-red-400 mt-0.5"
                        />

                        <p className="text-red-300 text-sm">

                          {item}

                        </p>
                      </div>
                    )
                  )}
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </motion.main>
  );
}

export default App;