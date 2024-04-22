from umodbus.serial import Serial as ModbusRTUMaster

# RTU Host/Master setup
# the following definition is for an ESP32
rtu_pins = (26, 27)         # (TX, RX)
uart_id = 1

host = ModbusRTUMaster(
    pins=rtu_pins,          # given as tuple (TX, RX)
    # baudrate=9600,        # optional, default 9600
    # data_bits=8,          # optional, default 8
    # stop_bits=1,          # optional, default 1
    # parity=None,          # optional, default None
    # ctrl_pin=12,          # optional, control DE/RE
    uart_id=uart_id         # optional, default 1, see port specific documentation
)

class  JGSmodbus_API() :
	def __init__(self,sladdr):
		self.sladdr=sladdr
		
# 03  host.read_holding_registers
	def read_sensor(self,startaddr,regqty,signed):
		try :
			sensor_status = host.read_holding_registers(slave_addr=self.sladdr, starting_addr=startaddr, register_qty=regqty, signed=signed)
			return sensor_status 
		except :
			pass 	


# 06 host.write_single_register
	def cmd_order(self,regaddr,regvalue,signed):
		try:
			on_status = host.write_single_register(slave_addr=self.sladdr, register_address=regaddr, register_value=regvalue, signed=signed)
			return on_status
		except :
			on_status = 0
			return on_status


