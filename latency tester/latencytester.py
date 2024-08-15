import time
from ping3 import ping, verbose_ping

def measure_latency(target, count=4):
  
    latencies = []
    packet_loss = 0
    
    for i in range(count):
        response = ping(target)
        if response is None:
            packet_loss += 1
        else:
            latencies.append(response * 1000)
        time.sleep(1)

    if latencies:
        average_latency = sum(latencies) / len(latencies)
    else:
        average_latency = None

    packet_loss_percentage = (packet_loss / count) * 100

    return average_latency, packet_loss_percentage

def display_results(target, average_latency, packet_loss_percentage):
    print(f"Latency Test Results for {target}:")
    if average_latency is not None:
        print(f"Average Latency: {average_latency:.2f} ms")
    else:
        print("No successful pings received.")
    print(f"Packet Loss: {packet_loss_percentage:.2f}%")

def main():
    target = input("Enter the server IP address or hostname: ")
    count = int(input("Enter the number of ping requests to send: "))
    
    average_latency, packet_loss_percentage = measure_latency(target, count)
    display_results(target, average_latency, packet_loss_percentage)

if __name__ == "__main__":
    main()
